# gh-action-commit-msg-match

## Example


```yml
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: checkout
        uses: actions/checkout@v2
      - name: skip or not
        id: skipornot
        uses: fcurella/gh-action-commit-msg-match
        with:
            matchWords: 'skip ci,release'
      - name: 'Some other job'
        id: waitforstatuschecks
        if: ${{ steps.skipornot.outputs.match == 'false' }}
        uses: "someuser/someimage"
```
