# issues

## pyrh

their auth doesnt work... read https://github.com/robinhood-unofficial/pyrh/issues/251

I did this and it still doesnt work. They probably need to rewrite the auth, maybe rh's auth api changed.

EDIT: yeah...shits broken son! They use an old API endpoint! see https://github.com/robinhood-unofficial/pyrh/issues/251#issuecomment-1100896232

EDIT2: It's not broken! They have an OLD RELEASE on PYPI...I was pulling an old version. I have updated `pyproject.toml` with my fork of pyrh to fix this.