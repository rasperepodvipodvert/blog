set OUTPUTDIR=site

set GITHUB_PAGES_REMOTE=gh-pages
set GITHUB_PAGES_BRANCH=gh-pages

mkdocs gh-deploy -m "Generate MkDocs site" -r %GITHUB_PAGES_REMOTE% -b %GITHUB_PAGES_BRANCH% -d %OUTPUTDIR% --force
rd site /S /Q