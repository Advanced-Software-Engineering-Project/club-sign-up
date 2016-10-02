/**
 * @jsx React.DOM
 */
var React = require('react')

var Success = React.createClass({
  render: function() {
    return (
      <div>
        <h2>Successfully Registered!</h2>
        <p>Thanks { this.props.fieldValues.name}!</p>
        <p>Please check your email <b>{this.props.fieldValues.email}</b> for updates.</p>
      </div>
    )
  }
})

module.exports = Success