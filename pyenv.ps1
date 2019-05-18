
# pyenv.ps1 应用于powershell命令行，在当前执行器中生效。

#Write-Output "$args $($args)"
#Write-Output "$args[0] $args[1] $args[2] $args[3]"
#Write-Output "$args[0] $($args[0])"
#Write-Output "$args[1] $($args[1])"
#Write-Output "$args[*] $args[-1] $($args[-1]) $_"
#Write-Output "$args.Split()"
#function sayHello
#{
#    if($args.Count -eq 0)
#    {
#        "No argument!"
#    }
#    else
#    {
#        $args | foreach {"Hello,$($_)"}
#        $args | foreach {"Hello,$_"}
#    }
#}
#sayHello $args

Set-Variable PYENVFLAG True
#Write-Output $PYENVFLAG

if ("$($args[0])" -eq "") {
    Write-Output usage:
    Write-Output "  pyenv <env-name>"
    Write-Output "  pyenv open <env-name>"
    Write-Output "  pyenv close <env-name>"
    Write-Output "  <env name>: 'current' is suggested."
    Write-Output ------
    Write-Output "please appoint a env name." ; exit 0
} elseif ("$($args[0])" -eq "open") {
    if ("$($args[1])" -eq "") {
        Write-Output usage:
        Write-Output "  pyenv <env-name>"
        Write-Output "  pyenv open <env-name>"
        Write-Output "  pyenv close <env-name>"
        Write-Output "  <env name>: 'current' is suggested."
        Write-Output ------
        Write-Output "please appoint a env name." ; exit 0
    }
    Set-Variable PYENVNAME $($args[1])
} elseif ("$($args[0])" -eq "close") {
    if ("$($args[1])" -eq "") {
        Write-Output usage:
        Write-Output "  pyenv <env-name>"
        Write-Output "  pyenv open <env-name>"
        Write-Output "  pyenv close <env-name>"
        Write-Output "  <env name>: 'current' is suggested."
        Write-Output ------
        Write-Output "please appoint a env name." ; exit 0
    }
    Set-Variable PYENVNAME $($args[1])
    Set-Variable PYENVFLAG False
} 
else {
    Set-Variable PYENVNAME $($args[0])
}

Set-Variable PYPROGRAMPATH $(Split-Path -Parent $MyInvocation.MyCommand.Definition)
Set-Variable PYPROGRAMNAME pymake.bat
Set-Variable PYPROGRAMPATHNAME $PYPROGRAMPATH/$PYPROGRAMNAME
#Write-Output "$(Split-Path -Parent $MyInvocation.MyCommand.Definition)"
#$PYPROGRAMPATHNAME

Write-Output "preparing env ..."

$PYENVINDEX = Get-Random
Write-Output "env index: [$PYENVINDEX]"

Invoke-Expression "$PYPROGRAMPATHNAME source root" | Set-Variable PYMMSOURCEROOT
Write-Output "location : [$PYMMSOURCEROOT]"

& "$PYPROGRAMPATHNAME" source config | Set-Variable PYMMSOURCECONFIG
Write-Output "configure: [$PYMMSOURCECONFIG] [1]"

& "$PYPROGRAMPATHNAME" get current env | Set-Variable PYMMDEFAULTENVNAME
echo "environme: [$PYMMDEFAULTENVNAME] [default]"

& "$PYPROGRAMPATHNAME" have env $PYENVNAME | Set-Variable PYENVEXISTEDFLAG
if ("$PYENVEXISTEDFLAG" -eq "False") {
    Write-Output "environme: [$PYENVNAME] is not existed."
    exit 0
}
Write-Output "environme: [$PYENVNAME] [$PYENVEXISTEDFLAG] [USED]"

& "$PYPROGRAMPATHNAME" get default exec root | Set-Variable PYMMSHELLROOT
Write-Output "exec root: [$PYMMSHELLROOT] [default]"

& "$PYPROGRAMPATHNAME" export2 powershell $PYENVNAME to $PYENVINDEX --custom

if ("$PYENVFLAG" -eq "False") {
    . "$PYMMSHELLROOT/${PYENVINDEX}_unset.ps1"
    Write-Output "user env : [$PYENVNAME] closed"
} 
else {
    . "$PYMMSHELLROOT/${PYENVINDEX}_effect.ps1"
    Write-Output "user env : [$PYENVNAME] opened"
}

#clean
Remove-Item -Force "$PYMMSHELLROOT/${PYENVINDEX}_effect.ps1","$PYMMSHELLROOT/${PYENVINDEX}_unset.ps1"

exit 0
