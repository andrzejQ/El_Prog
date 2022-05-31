<#
Kanały i częstotliwości - Standard D/K (CCIR) - wynik w "tvMHz_.csv"
#>
Set-StrictMode -Version 3
$PSDefaultParameterValues['Out-File:Encoding'] = 'UTF8'
$outCsv = "tvMHz_.csv"
$maxMHz = 862

$bands = @(
  [PSCustomObject]@{ CSE='C'; Nr=21; F0=470.0; dF=8.0 },
  [PSCustomObject]@{ CSE='S'; Nr= 9; F0=230.0; dF=8.0 },
  [PSCustomObject]@{ CSE='E'; Nr= 5; F0=174.0; dF=7.0 },
  [PSCustomObject]@{ CSE='S'; Nr= 1; F0=110.0; dF=8.0 },
  [PSCustomObject]@{ CSE='?'; Nr= 0; F0=0.0; dF=110.0 }
)

( $s = "C;MHz" )
$out = ,$s

foreach ($j in ($bands.Length-2)..0) {
  $maxF = if ( $j -eq 0 ) { $maxMhz } else { $bands[$j-1].F0 } 
  $b = $bands[$j]
  $MHz = $b.F0+$b.dF/2
  $i = $b.Nr
  while ($MHz -lt $maxF) {
    ( $s = $b.CSE+$i+";"+$MHz )
    $out += $s
    $i++
    $MHz += $b.dF
  }
}
Write-Host `n '- zob.' $outCsv
$out > $outCsv