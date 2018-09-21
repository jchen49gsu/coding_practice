# coding_practice for Algorithm interview

Push the changes in your local repository to GitHub.

### git pull --rebase
### git push -u origin master
#### Pushes the changes in your local repository up to the remote repository you specified as the origin



## Python "sum" - Convert list-of-lists to a list
```python
lists_list = [ [1, 2], [3, 4], [5, 6] ]
tuples_list = [ (1, 2, 3), (4, 5, 6) ]
alist = list(sum(lists_list, []))
alist = list(sum(tuples_list, ()))   =>same 
=> alist = [1, 2, 3, 4, 5, 6]
