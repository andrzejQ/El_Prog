<#
Po wyszukaniu kanałów w programie SichboPVR -> https://sichbopvr.com/pl-pl/
powstaje plik "%ProgramData%\SichboPVR4\service-channels.json",
z aktualną informacją o dostępnych kanałach DVB-T/T2 - wynik w "chInfo_.csv"
#>
Set-StrictMode -Version 3
$PSDefaultParameterValues['Out-File:Encoding'] = 'UTF8'
$outCsv = "chInfo_.csv"

$serviceChannels = Get-Content -Path "C:\ProgramData\SichboPVR4\service-channels.json" | ConvertFrom-Json
$Transponders = $serviceChannels.Transponders
$Channels = $serviceChannels.Channels 

$bands = @(
  [PSCustomObject]@{ CSE='C'; Nr=21; F0=470.0; dF=8.0 },
  [PSCustomObject]@{ CSE='S'; Nr= 9; F0=230.0; dF=8.0 },
  [PSCustomObject]@{ CSE='E'; Nr= 5; F0=174.0; dF=7.0 },
  [PSCustomObject]@{ CSE='S'; Nr= 1; F0=110.0; dF=8.0 },
  [PSCustomObject]@{ CSE='?'; Nr= 0; F0=0.0; dF=110.0 }
)
function cTV { param ($MHz_) # cTV(474) -> "C21"; cTV(177.5) -> "E5"
  $MHz = $MHz_ -as [double]; if (($null -eq $MHz) -or ($MHz -lt 0.0)) { $MHz = 0.0 }
  foreach ($b in $bands) {
    if ($MHz -gt $b.F0) { break }
  }
  $b.CSE + [Math]::Floor( $b.Nr + ($MHz-$b.F0)/$b.dF )
}  
# Transponders/1?/Info  #  "Info": "dvbt2 690 8 -1",
# Channels/3?/Name/s/0/v  #  Science Poland HD
# Channels/3?/Streams/0?/Video/Height  #  1080
( $s = "nazwa;h;C;t2;MHz;8;1" )
$out = ,$s
foreach ($ch in $Channels) {
  $transp = (($Transponders | where {$_.UID -eq $ch.TransponderUID}).info).Split(' ')
  $C = cTV $transp[1] 
  ( $s = @( $ch.Name.s[0].v ,
           ($ch.Streams | where {[bool] $_.psobject.Properties['Video']} | select -First 1).Video.Height ,
            $C 
         ) + $transp `
         -join ";" )
  $out += $s
}                       #'Science Poland HD;1080;C48;dvbt2;690;8;-1'

Write-Host `n($out.Length-1) 'kanałów - zob.' $outCsv
$out > $outCsv
