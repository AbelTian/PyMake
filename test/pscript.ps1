function test_ping($iplist)
{
    foreach ($myip in $iplist)
    {
        $strQuery = "select * from win32_pingstatus where address = '$myip'"
        # 这里是中文，请不要乱码。
        $wmi = Get-WmiObject -query $strQuery
        if ($wmi.statuscode -eq 0) 
        {
            return "Pinging`t$myip...`tsuccessful"
        }
        else 
        {
            return "Pinging`t$myip...`tErrorCode:" + $wmi.statuscode
        }
    }
}

test_ping args[0]
$env:MYVAR="BHGNG"
echo "xxxxx $env:MYVAR"

remove-item env:MYVAR
echo "xxxxx $env:MYVAR"

$env:MYVAR = "GGGGG"
echo "bbbbbb $env:MYVAR"

$env:MYVAR = ""
echo "bbbbbb $env:MYVAR"

remove-item env:MYVAR

$env:Path = "R:\Develop;" + $env:Path
echo  $env:Path

#$oldstr = $env:Path -split ";"
#$env:path = $oldstr - "R:\Develop"
#echo $env:Path

echo ------------------------------------
$env:Path = $env:Path.Insert(0, "V:/Develop;")
echo $env:Path

echo ********************************
if ( $env:Path.Contains("V:/Develop;" ) ) { $env:Path = $env:Path.Replace("V:/Develop;", "") }
$env:Path = $env:Path.Replace("V:\Develop;", "")
$env:Path = $env:Path.Replace("R:\Develop;", "")
echo $env:Path

echo "AAAAAAAAAAAAA $env:MYVAR"
if ( !$env:Path.Contains("V:/Develop;" ) ) { 
    echo ........... 
}

echo 这里是中文，请不要乱码。
Write-Host "Hello,$args"