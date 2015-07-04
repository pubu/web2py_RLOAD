# web2py_RLOAD
use react.js view generation inside web2py with RLOAD()

# How it work

If you call a function by a request inside web2py, where RLOAD() is placed you will get following output

call:
/default/index

```html
  <script>
    var viewData = {{=viewData #JSON}}
  </script>
 
  <div data-w2p_react_remote="default/index.jsx" id="c398468477432">bitte warten ...</div>
 
  <script>
    compliled react.js JSX (/default/index.jsx)
  </script>
 ```
viewData comes from default/index
