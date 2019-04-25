#!/usr/bin/env bash

cd /Users/abel/Develop/b0-toolskits/macLibraries/Qt/4.8.7/clang_64/lib

export qtmodule=Qt3Support\ QtCore\ QtDBus\ QtDeclarative\ QtDesigner\ QtDesignerComponents\ QtGui\ QtHelp\ QtMultimedia\ QtNetwork\ QtOpenGL\ QtScript\ QtScriptTools\ QtSql\ QtSvg\ QtTest\ QtWebKit\ QtXml\ QtXmlPatterns\ phonon

#echo $qtmodule

for var in $qtmodule
do
    #echo a $var
    for recur in $qtmodule
    do
        #echo b $recur
        echo install_name_tool -change ${recur}.framework/Versions/4/${recur} @rpath/${recur}.framework/Versions/4/${recur} ${var}.framework/Versions/4/${var}
    done
done

cd /Users/abel/Develop/b0-toolskits/macLibraries/Qt/4.8.7/clang_64/bin

export qtapp=Assistant\ Designer\ Linguist\ QMLViewer\ pixeltool\ qdbusviewer\ qhelpconverter\ qtdemo

for var in $qtapp
do
    #echo a $var
    for recur in $qtmodule
    do
        #echo b $recur
        echo install_name_tool -change ${recur}.framework/Versions/4/${recur} @rpath/${recur}.framework/Versions/4/${recur} ${var}.app/Contents/MacOS/${var}
    done
done

export qtexe=$(ls)

for var in $qtexe
do
    #echo a $var
    for recur in $qtmodule
    do
        #echo b $recur
        echo install_name_tool -change ${recur}.framework/Versions/4/${recur} @rpath/${recur}.framework/Versions/4/${recur} ${var}
    done
done

for var in $qtexe
do
    #install_name_tool -rpath ../lib @executable_path/../lib ${var}
    #install_name_tool -delete_rpath @executable_path/../lib ${var}
    echo install_name_tool -add_rpath @executable_path/../lib ${var}
done

export qt_mod=macdeployqt\ macchangeqt

for var in $qt_mod
do
    #echo a $var
    for recur in $qtmodule
    do
        #echo b $recur
        install_name_tool -add_rpath @executable_path/../lib ${var}
        install_name_tool -change ${recur}.framework/Versions/4/${recur} @rpath/${recur}.framework/Versions/4/${recur} ${var}
    done
done
