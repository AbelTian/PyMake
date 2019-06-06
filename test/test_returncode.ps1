echo 这里是中文，请不要乱码。
Write-Host "Hello,$args"
Write-Host "args[0] $($args[0])"
Write-Host "args[1] $($args[1])"
Write-Host "args[2] $($args[2])"
Write-Host "args[3] $($args[3])"
Write-Host "args[4] $($args[4])"
Write-Host "args[5] $($args[5])"
Write-Host "args[6] $($args[6])"
Write-Host "args[7] $($args[7])"
Write-Host "args[8] $($args[8])"
Write-Host "args[9] $($args[9])"

Write-Output "This will exit with 5, please see it with echo `$LASTEXITCODE"
exit 5