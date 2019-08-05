echo off

set initpath=%1
set ldrapath1=%2
set vvpath=%3
set ldrapath2=%4

copy "%initpath%\TESTBED.ini" "%initpath%\TESTBED_backup.ini"
rem Project settings
start /wait %ldrapath1%\tbini.exe -Section="C/C++ LDRA Testbed" SYSEARCH_FILE="%vvpath%\sysearch_VPMAB.dat"

start /wait %ldrapath1%\tbini.exe -Section="C/C++ LDRA Testbed" SYSPPVAR_FILE="%vvpath%\sysppvar_VPMA.dat"

rem Coverage Settings

start /wait %ldrapath1%\tbini.exe -Section="C/C++ LDRA Testbed" DYNAMIC_REPORT_CONFIGURATION=Custom

start /wait %ldrapath1%\tbini.exe -Section="C/C++ LDRA Testbed" DEFAULT_CUSTOM_SETTINGS="0 1 1 1 0 0 0 1"

start /wait %ldrapath1%\tbini.exe -Section="C/C++ LDRA Testbed" DEFAULT_COVERAGE_METRICS="100 100 100 "

rem infiniteloop settings
start /wait %ldrapath1%\tbini.exe -Section="C/C++ LDRA Testbed" TBRUN_ENABLE_CREATE_TC_THROUGH_THREAD=TRUE

start /wait %ldrapath1%\tbini.exe -Section="C/C++ LDRA Testbed" TBRUN_NODOTDOTDOT=TRUE

start /wait %ldrapath1%\tbini.exe -Section="C/C++ LDRA Testbed" TBRUN_NULL=(char*)(0)

start /wait %ldrapath1%\tbini.exe -Section="C/C++ LDRA Testbed" TBRUN_TC_SETJMP=TRUE

start /wait %ldrapath1%\tbini.exe -Section="C/C++ LDRA Testbed" TBRUN_LOCAL_STUB_HIT_COUNTS=TRUE


start /wait %ldrapath1%\tbini.exe -Section="C/C++ Microsoft Visual C/C++ v6.0 Build Environment" INCLUDE=%ldrapath2%

