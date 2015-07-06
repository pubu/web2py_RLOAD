# web2py_RLOAD
use react.js view generation inside web2py with RLOAD()

The idea behind RLOAD is to use nice MC from web2py and use react.js View handeling, to extend the way of creating web-components (LOAD) inside web2py. 

the counterpart is you need node and react installed to do jsx translation
```bash
npm install --save react react-render babel-core babel-loader
pip install react
```
# How it work

{{=RLOAD(url_to.jsx, mount_point, content="bitte warten ...")}}

will create following output

```html
<div data-w2p_react_remote="url.jsx" id="random-id">bitte warten ...</div>
<script>
  var viewData = data; <- set by function call inside web2py
  var modelData = model; <- set by function call inside web2py
</script>
<script>
... compliled react.js JSX (url.jsx) ...

React.render(
	<OwnComponent url="{{=url}}" />,
	document.getElementById('random-id')
)
</script>
 ```

content inside .html view will ignored by RLOAD call.
