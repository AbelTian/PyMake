``` json  

"Tips": {
    "path-assemblage": {
        "Tips": "All path are located in this group.",
        "p1": "a path on computer",
        "p2": "${p1}/a sub path under p1"
    },
    "environ": {
        "default": {
            "path+": [
                "path+ paths will be added to default env path.",
                "${p2}"
                "I add p2 to default env path."
            ],
            "Tips1": "Tips1 variables will be added to default env.",
            "Tips2": "Current env is default.",
            "VAR1":"a variable",
            "VARXXX": "${VAR1} param3",
            "VARP3": "${p2}/VAR0",
            "Tips2": "You can use ${var-name} in path-assemblage and this environ to abb variables.",
            "a_special_var_const": "hello world"
        },
        "env-name": {
            "path+": [
                "an important path",
                "path+ paths will be added to default env path.",
                "${p2}"
                "I add p2 to default env path."
            ],
            "AN_IMPORTANT_VARIABLE": "My Name",
            "Tips1": "Tips1 variables will be added to default env.",
            "Tips2": "Current env is default.",
            "VAR1":"a variable",
            "VARXXX": "${VAR1} param3",
            "VARP3": "${p2}/VAR0",
            "Tips2": "You can use ${var-name} in path-assemblage and this environ to abb variables.",
            "a_special_var_const": "hello world"
        },
        "current": "default"
    },
    "command": {
        "command-name": [
            "All commands are here, they will be executed step by step.",
            "This is a command, step 2",
            "${p2}/cmd2 ${VARXXX}",
            "You can use ${var-name} in path-assemblage and current environ to abb command line content."
        ],
        "command-name-2": [
            "All commands are here, they will be executed step by step.",
            "This is a command, step 2",
            "${p2}/cmd2 ${VARXXX}",
            "You can use ${var-name} in path-assemblage and current environ to abb command line content."
        ]
    },
    "Tips": "User can delete these Tips group."
}

```