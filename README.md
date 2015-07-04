# web2py_RLOAD
use react.js view generation inside web2py with RLOAD()

# How it work

If you call a function by a request inside web2py, where RLOAD() is placed you will get following output

call:
/default/index
<code>
  <script>
    var viewData = {{=viewData #JSON}}
  </script>
  <script>
    compliled react.js JSX (/default/index.jsx)
  </script>
</code>
viewData comes from default/index
