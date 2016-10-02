/**
 * @jsx React.DOM
 */
var React                   = require('react')
var getRadioOrCheckboxValue = require('../lib/radiobox-value')

var SurveyFields = React.createClass({

  renderOptions: function(type, name, value, index) {
    var isChecked = function() {
      if (type == 'radio') return value == this.props.fieldValues[name]

      if (type == 'checkbox') return this.props.fieldValues[name].indexOf(value) >= 0

      return false
    }.bind(this)

    return (
      <label key={index}>
        <input type={type} name={name} value={value} defaultChecked={isChecked()} /> {value}
      </label>
    )
  },

  render: function() {
    return (
      <div>
        <h2>Questions</h2>
        <ul className="form-fields">
          <li className="radio">
            <span className="label">School</span>
            {['School of Engineering and Applied Sciences', 'General Studies', 'Columbia College', 'Barnard'].map(this.renderOptions.bind(this, 'radio', 'school'))}
          </li>
          <li className="radio">
            <span className="label">Graduating Year</span>
            {['2017', '2018', '2019', '2020'].map(this.renderOptions.bind(this, 'radio', 'grad_year'))}
          </li>
          <li className="checkbox">
            <span className="label">Email Preferences</span>
            {['I want to become a member of the group.', 'Email me about upcoming events.'].map(this.renderOptions.bind(this, 'checkbox', 'preference'))}
          </li>
          <li className="form-footer">
            <button className="btn -default pull-left" onClick={this.props.previousStep}>Back</button>
            <button className="btn -primary pull-right" onClick={this.nextStep}>Save &amp; Continue</button>
          </li>
        </ul>
      </div>
    )
  },

  nextStep: function() {
    // Get values via querySelector
    var school    = document.querySelector('input[name="school"]:checked')
    var grad_year = document.querySelector('input[name="grad_year"]:checked')
    var preference = document.querySelectorAll('input[name="preference"]')

    var data = {
      school    : getRadioOrCheckboxValue(school),
      grad_year : getRadioOrCheckboxValue(grad_year),
      preference : getRadioOrCheckboxValue(preference)
    }

    this.props.saveValues(data)
    this.props.nextStep()
  }
})

module.exports = SurveyFields