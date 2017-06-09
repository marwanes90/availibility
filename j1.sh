git log --pretty=format:'%h' | while read revision
    do date=$( git show --summary --pretty=%aI $revision | head -n 1)
    git show $revision:report.json > revision_"$date".json
done