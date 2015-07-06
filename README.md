# web2py_RLOAD
use react.js view generation inside web2py with RLOAD()

# How it work

{{=RLOAD(url, mount_point, content="bitte warten ...")}}

will create following output

```html
<div data-w2p_react_remote="url.jsx" id="random-id">bitte warten ...</div>
<script>
  var viewData = data; <- set by function call inside web2py
  var modelData = model; <- set by function call inside web2py
</script>
<script>
  compliled react.js JSX (url.jsx)
</script>
 ```
viewData comes from default/index
