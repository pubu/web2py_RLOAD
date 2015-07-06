# web2py_RLOAD
use react.js view generation inside web2py with RLOAD()

The idea behind RLOAD is to use nice MC from web2py and react.js View handeling, to extend the way of creating web-components inside web2py. 

The greate LOAD function inside web2py, which i was using before knowing of react doing great job in handling dynamic html parts. 

## why i trying in using react.js? 
I thinging this is next step for creating complex interfaces, where javascript is handling the big part of user interaction. 

## requirements
the counterpart is you need node and react installed to do jsx translation
```bash
npm install --save react react-render babel-core babel-loader
pip install react
```
# how it work

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
