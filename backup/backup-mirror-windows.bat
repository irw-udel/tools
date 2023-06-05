::========================================
:: MIT License
:: Set parameters for instrument name, source, archive, and maxage (date or number of days)
:: Note: this will delete files in the archive if they are not in the source folder
::========================================

SETLOCAL
SET INSTRUMENT_NAME=""
SET SRC=D:\
SET ARCH="C:\path\to\archive"
SET XFName=*backup*.log
SET XDName="*System Volume Information*" "$RECYCLE.BIN"
SET BACKUP_DATE=%DATE:~10,4%%DATE:~4,2%

SET LOG=%ARCH%\_backup_%INSTRUMENT_NAME%_%BACKUP_DATE%.log
SET OPT=/mir /r:5 /w:15 /log+:%LOG% /xf %XFName% /xd %ARCH% %XDName% /mt /maxage:YYYYMMDD
SET CMD=robocopy %SRC% %ARCH% %OPT%
%CMD%