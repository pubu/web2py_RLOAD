var TodoList = React.createClass({
  render: function() {
  	/*
	 * render TodoList
  	*/
    var todos = this.props.data.map(function (todo) {
      return (
        <li>
          {todo.txt} {todo.due_date} 
        </li>
      );
    });
    return (
      <ul className="todolist">
        {todos}
      </ul>
    );
  }
});


var Web2pyFormInput = React.createClass({

	// Add the Formsy Mixin
	mixins: [Formsy.Mixin],

	// setValue() will set the value of the component, which in 
	// turn will validate it and the rest of the form
	changeValue: function (event) {
	  this.setValue(event.currentTarget.value);
	},
	render: function () {

	  // Set a specific className based on the validation
	  // state of this component. showRequired() is true 
	  // when the value is empty and the required prop is 
	  // passed to the input. showError() is true when the 
	  // value typed is invalid
	  var className = this.showRequired() ? 'required' : this.showError() ? 'error' : null;

	  // An error message is returned ONLY if the component is invalid
	  // or the server has returned an error message
	  var errorMessage = this.getErrorMessage();

  	  var fldId = 'fld-' + this.props.name;

	  return (
	    <div className={className}>
	      <label htmlFor={fldId}><span>{this.props.config.label}</span></label>
	      <input type={this.props.config.type} id={fldId} placeholder={this.props.config.label} required={this.props.config.required}  onChange={this.changeValue} value={this.getValue()}/>
	      <span>{errorMessage}</span>
	    </div>
	  );
	}
});

var TodoForm = React.createClass({
  getInitialState: function() {
    return {
    			canSubmit: true,
    			modelData: modelData
    		};
  },
  submit : function(data) {
	this.props.listData.push(data);
	this.props.setData(this.props.listData);
	this.setState({
	    canSubmit: true
	});
  },
  enableButton: function () {
	  this.setState({
	    canSubmit: true
	  });
  },
  disableButton: function () {
	  this.setState({
	    canSubmit: false
	  });
  },
  render: function() {
  	/*
	 * render Todobox
  	*/

  	var fieldSet = this.state.modelData.map(function(fld){
  		return (
  				<Web2pyFormInput name={fld.name} config={fld} />
  			)
  	});

    return (
      <Formsy.Form className="todoform" onValidSubmit={this.submit} onValid={this.enableButton} onInvalid={this.disableButton}>
      	<fieldset>
      	{fieldSet}
      	</fieldset>
      	<div className="action">
      		<button className="btn-primary" type="submit" disabled={!this.state.canSubmit}>Submit</button>
      	</div>
      </Formsy.Form>
    );
  }
});

var TodoBox = React.createClass({
  getInitialState: function() {
    return {data: viewData};
  },
  setData : function(data){
  	console.log(data);
  	this.setState({data:data});
  },
  render: function() {
  	/*
	 * render Todobox
  	*/
    return (
      <div className="todobox">
        <TodoList data={this.state.data} />
        <TodoForm setData={this.setData} listData={this.state.data} />
      </div>
    );
  }
});

React.render(
	<TodoBox url="{{=url}}" />,
	document.getElementById('{{=cid}}')
)

