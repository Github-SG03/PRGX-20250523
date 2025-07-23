set CD=%CD%
for /f %%m in ('dir /b *.*') do (gawk -F"|" "{ print NF }" %%m > %%m_FIELDS_PER_LINE.txt)
pause