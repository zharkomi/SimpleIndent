# Simple Indent Sublime Plugin
Sublime plugin to indent any code with brackets

If you have a string which represents a hierarchical structure like this:

```string
Node{id=1, name='Root', children=[Node{id=2, name='Child 1', children=[Node{id=4, name='Grandchild 1.1', children=[]}, Node{id=5, name='Grandchild 1.2', children=[]}]}, Node{id=3, name='Child 2', children=[]}]}  
{"id":1,"name":"Root","children":[{"id":2,"name":"Child 1","children":[{"id":4,"name":"Grandchild 1.1","children":[]},{"id":5,"name":"Grandchild 1.2","children":[]}]},{"id":3,"name":"Child 2","children":[]}]}
```

This plugin will format it based on brackets without validating any structure:

```
Node{
  id=1,
   name='Root',
   children=[
    Node{
      id=2,
       name='Child 1',
       children=[
        Node{
          id=4,
           name='Grandchild 1.1',
           children=[]
        },
         Node{
          id=5,
           name='Grandchild 1.2',
           children=[]
        }
      ]
    },
     Node{
      id=3,
       name='Child 2',
       children=[]
    }
  ]
}  
{
  "id":1,
  "name":"Root",
  "children":[
    {
      "id":2,
      "name":"Child 1",
      "children":[
        {
          "id":4,
          "name":"Grandchild 1.1",
          "children":[]
        },
        {
          "id":5,
          "name":"Grandchild 1.2",
          "children":[]
        }
      ]
    },
    {
      "id":3,
      "name":"Child 2",
      "children":[]
    }
  ]
}
```
Simple configuration:
```json
{
  "open_brackets": "{([",
  "close_brackets": "})]",
  "new_line": ",",
  "tab_str": "  "
}
```