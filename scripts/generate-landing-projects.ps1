[CmdletBinding()]
param(
  [string]$RepoRoot = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not $RepoRoot) {
  $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
  $RepoRoot = (Resolve-Path (Join-Path $scriptDir "..")).Path
}

function Get-NormalizedRelativePath {
  param(
    [string]$BasePath,
    [string]$FullPath
  )
  $relative = $FullPath.Substring($BasePath.Length).TrimStart("\", "/")
  return ($relative -replace "\\", "/")
}

function Get-DefaultBullets {
  param([string]$Sector)

  switch ($Sector) {
    "oilgas" {
      return @(
        "Ingenieria, procura y construccion EPC",
        "Integracion electrica y de control",
        "Comisionamiento y puesta en marcha"
      )
    }
    "energia" {
      return @(
        "Infraestructura electrica BT/MT/AT",
        "Pruebas, proteccion y energizacion",
        "Ejecucion integral en campo"
      )
    }
    default {
      return @(
        "Diseno e integracion multimarcas",
        "Implementacion y arranque en sitio",
        "Soporte para continuidad operativa"
      )
    }
  }
}

function Get-TitleFromFilename {
  param([string]$FileName)

  $base = [System.IO.Path]::GetFileNameWithoutExtension($FileName)
  $title = $base -replace "[_-]+", " "
  $title = $title -replace "\s+", " "
  $title = $title.Trim()
  return (Get-Culture).TextInfo.ToTitleCase($title.ToLower())
}

$projectsRoot = Join-Path $RepoRoot "assets\img\Projects"
$outputPath = Join-Path $RepoRoot "assets\data\landing-projects.json"
$overridePath = Join-Path $RepoRoot "assets\data\landing-project-overrides.json"

$sectorFolders = @(
  @{ Sector = "oilgas"; RelativePath = "oil&gas" },
  @{ Sector = "energia"; RelativePath = "infraestructura_electrica" },
  @{ Sector = "industrial"; RelativePath = "Soluciones_industriales" }
)

$overridesByImage = @{}
if (Test-Path $overridePath) {
  $overrideItems = Get-Content -Raw -Path $overridePath | ConvertFrom-Json
  foreach ($item in $overrideItems) {
    if (-not $item.img) { continue }
    $key = [string]$item.img
    $key = $key.Replace("\", "/").ToLowerInvariant()
    $overridesByImage[$key] = $item
  }
}

$projectItems = New-Object System.Collections.Generic.List[object]

foreach ($folder in $sectorFolders) {
  $sector = [string]$folder.Sector
  $absFolder = Join-Path $projectsRoot ([string]$folder.RelativePath)
  if (-not (Test-Path $absFolder)) { continue }

  $files = Get-ChildItem -Path $absFolder -File |
    Where-Object { $_.Extension -match '^\.(png|jpg|jpeg|webp|avif)$' } |
    Sort-Object Name

  foreach ($file in $files) {
    $img = Get-NormalizedRelativePath -BasePath $RepoRoot -FullPath $file.FullName
    $lookupKey = $img.ToLowerInvariant()
    $override = $null
    if ($overridesByImage.ContainsKey($lookupKey)) {
      $override = $overridesByImage[$lookupKey]
    }

    $title = if ($override -and $override.title) { [string]$override.title } else { Get-TitleFromFilename -FileName $file.Name }
    $bullets = if ($override -and $override.bullets) {
      @($override.bullets | ForEach-Object { [string]$_ })
    } else {
      Get-DefaultBullets -Sector $sector
    }

    $projectItems.Add([ordered]@{
      sector  = $sector
      title   = $title
      img     = $img
      bullets = $bullets
    })
  }
}

$outputDir = Split-Path -Parent $outputPath
if (-not (Test-Path $outputDir)) {
  New-Item -ItemType Directory -Path $outputDir | Out-Null
}

$json = $projectItems | ConvertTo-Json -Depth 6
Set-Content -Path $outputPath -Value $json -Encoding UTF8

Write-Host ("Manifest generated: {0} items -> {1}" -f $projectItems.Count, $outputPath)
