from flask import Flask, render_template, redirect, request, flash
from wtforms import Form, IntegerField, StringField, SelectField, validators
from wtforms.validators import DataRequired
import sys

app = Flask(__name__)
# form-logic

workclass_choices = [('1', 'Private'), ('2', 'Self-emp-not-inc'), ('3', 'Federal-gov'),
					 ('4', 'Local-gov'), ('5', 'State-gov'), ('6', 'Without-pay'),
					 ('7', 'Never-worked')
					]

education_choices = [('1', 'Bachelors'), ('2', 'Some-college'), ('3', '11th'),
					 ('4', 'HS-grad'), ('5', 'Prof-school'), ('6', 'Assoc-acdm'),
					 ('7', 'Assoc-avoc'), ('8', '9th'), ('8', '7th-8th'), 
					 ('9', '12th'), ('10', 'Masters'), ('11', '1st-4th'),
					 ('12', '10th'), ('13', 'Doctorate'), ('14', '5th-6th'),
					 ('15', 'Preschool')
					]

marital_choices = [('1', 'Married-civ-spouse'), ('2', 'Divorced'), ('3', 'Never-married'),
					 ('4', 'Separated'), ('5', 'Widowed'), ('6', 'Married-spouse-absent'),
					 ('7', 'Married-AF-spouse')
					]

occupation_choices = [('1', 'Tech-support'), ('2', 'Craft-repair'), ('3', 'Other-service'),
					 ('4', 'Sales'), ('5', 'Exec-managerial'), ('6', 'Prof-specialty'),
					 ('7', 'Machine-op-inspct'), ('8', 'Adm-clerical'), ('9', 'Farming-fishing'),
					 ('10', 'Transport-moving'), ('11', 'Priv-house-serv'), ('12', 'Protective-serv'),
					 ('13', 'armed-Forces')
					]

relationship_choices = [('1', 'Wife'), ('2', 'Own-child'), ('3', 'Husband'),
					 ('4', 'Not-in-familty'), ('5', 'Other-relative'), ('6', 'Unmarried')
					]

race_choices = [('1', 'White'), ('2', 'Asian-Pac-Islander'), ('3', 'Amer-Indian-Eskimo'),
					 ('4', 'Other'), ('5', 'Black')
					]

sex_choices = [('1', 'Female'), ('2', 'Male')]

native_country_choices = [('1', 'United-States'), ('2', 'Cambodia'), ('3', 'England'),
					 ('4', 'Puerto-Rico'), ('5', 'Canada'), ('6', 'Germany'),
					 ('7', 'Outlying-US(Guam-USVI-etc)'), ('8', 'India'), ('9', 'Japan'),
					 ('10', 'Greece'), ('11', 'South'), ('12', 'China'),
					 ('13', 'Cuba'), ('14', 'Iran'), ('15', 'Honduras'), ('16', 'Philippines'), ('17', 'Italy'),
					 ('18', 'Poland'), ('19', 'Jamaica'), ('20', 'Vietnam'), ('21', 'Mexico'), ('22', 'Portugal'),
					 ('23', 'Ireland'), ('24', 'France'), ('25', 'Dominican-Republic'), ('26', 'Laos'), ('27', 'Ecuador'),
					 ('28', 'Taiwan'), ('29', 'Haiti'), ('30', 'Columbia'), ('31', 'Hungary'), ('32', 'Guatemala'),
					 ('33', 'Nicaragua'), ('34', 'Scotland'), ('35', 'Thailand'), ('36', 'Yugoslavia'), ('37', 'El-Salvador'),
					 ('38', 'Trinadad&Tobago'), ('39', 'Peru'), ('40', 'Hong'), ('41', 'Holand-Netherlands') 
					]

class InputForm(Form):
	age = StringField('Age')
	workclass = SelectField('Workclass', choices = workclass_choices)
	fnlwgt = StringField('Final Weight')
	education = SelectField('Education', choices = education_choices)
	education_num = StringField('Education Num')
	marital_status = SelectField('Marital Status', choices = marital_choices)
	occupation = SelectField('Occupation', choices = occupation_choices)
	relationship = SelectField('Relationship', choices = relationship_choices)
	race = SelectField('Race', choices = race_choices)
	sex = SelectField('Sex', choices = sex_choices)
	capital_gain = StringField('Capital Gain')
	capital_loss = StringField('Capital Loss')
	hours_per_week = StringField('Hours per Week')
	native_country = SelectField('Native Country', choices = native_country_choices)

# routing
@app.route('/', methods=('GET', 'POST'))
def index():
	form = InputForm(request.form)
	if (request.method == 'POST'):
		
		age_value = form.age.data
		fnlwgt_value = form.fnlwgt.data
		education_num_value = form.education_num.data
		capital_gain_value = form.capital_gain.data
		capital_loss_value = form.capital_loss.data
		hours_per_week_value = form.hours_per_week.data

		workclass_value = dict(workclass_choices).get(form.workclass.data)
		education_value = dict(education_choices).get(form.education.data)
		marital_status_value = dict(marital_choices).get(form.marital_status.data)
		occupation_value = dict(occupation_choices).get(form.occupation.data)
		relationship_value = dict(relationship_choices).get(form.relationship.data)
		race_value = dict(race_choices).get(form.race.data)
		sex_value = dict(sex_choices).get(form.sex.data)
		native_country_value = dict(native_country_choices).get(form.native_country.data)

		value = [age_value, workclass_value,fnlwgt_value, education_value,
				education_num_value, marital_status_value, occupation_value,
				relationship_value, race_value, sex_value, capital_gain_value,
				capital_loss_value, hours_per_week_value, native_country_value
				]
		flash(value, 'success')
		return redirect('/')
	return render_template('index.html', form=form)

if __name__ == '__main__':
	app.secret_key = 'The-Capitalist'
	app.run() 