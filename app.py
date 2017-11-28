from flask import Flask, render_template, redirect, request, flash
from wtforms import Form, IntegerField, StringField, SelectField, validators
from wtforms.validators import DataRequired
import numpy as np
from sklearn.externals import joblib
import sys

app = Flask(__name__)
# form-logic

workclass_choices = [(3, 'Private'), (5, 'Self-emp-not-inc'), (0, 'Federal-gov'),
					 (1, 'Local-gov'), (6, 'State-gov'), (7, 'Without-pay'),
					 (2, 'Never-worked')
					]

education_choices = [(9, 'Bachelors'), (15, 'Some-college'), (1, '11th'),
					 (11, 'HS-grad'), (14, 'Prof-school'), (7, 'Assoc-acdm'),
					 (8, 'Assoc-avoc'), (6, '9th'), (5, '7th-8th'), 
					 (2, '12th'), (12, 'Masters'), (3, '1st-4th'),
					 (0, '10th'), (10, 'Doctorate'), (4, '5th-6th'),
					 (13, 'Preschool')
					]

marital_choices = [(2, 'Married-civ-spouse'), (0, 'Divorced'), (4, 'Never-married'),
					 (5, 'Separated'), (6, 'Widowed'), (3, 'Married-spouse-absent'),
					 (1, 'Married-AF-spouse')
					]

occupation_choices = [(13, 'Tech-support'), (3, 'Craft-repair'), (8, 'Other-service'),
					 (12, 'Sales'), (4, 'Exec-managerial'), (10, 'Prof-specialty'), (6, 'Handlers-cleaners'),
					 (7, 'Machine-op-inspct'), (1, 'Adm-clerical'), (5, 'Farming-fishing'),
					 (14, 'Transport-moving'), (9, 'Priv-house-serv'), (11, 'Protective-serv'),
					 (2, 'armed-Forces')
					]

relationship_choices = [(5, 'Wife'), (3, 'Own-child'), (0, 'Husband'),
					 (1, 'Not-in-familty'), (2, 'Other-relative'), (4, 'Unmarried')
					]

race_choices = [(4, 'White'), (1, 'Asian-Pac-Islander'), (0, 'Amer-Indian-Eskimo'),
					 (3, 'Other'), (2, 'Black')
					]

sex_choices = [(0, 'Female'), (1, 'Male')]

native_country_choices = [(38, 'United-States'), (0, 'Cambodia'), (8, 'England'),
					 (32, 'Puerto-Rico'), (1, 'Canada'), (10, 'Germany'),
					 (27, 'Outlying-US(Guam-USVI-etc)'), (18, 'India'), (23, 'Japan'),
					 (11, 'Greece'), (34, 'South'), (2, 'China'),
					 (4, 'Cuba'), (19, 'Iran'), (15, 'Honduras'), (29, 'Philippines'), (21, 'Italy'),
					 (30, 'Poland'), (22, 'Jamaica'), (39, 'Vietnam'), (25, 'Mexico'), (31, 'Portugal'),
					 (20, 'Ireland'), (9, 'France'), (5, 'Dominican-Republic'), (24, 'Laos'), (6, 'Ecuador'),
					 (35, 'Taiwan'), (13, 'Haiti'), (3, 'Columbia'), (17, 'Hungary'), (12, 'Guatemala'),
					 (26, 'Nicaragua'), (33, 'Scotland'), (36, 'Thailand'), (40, 'Yugoslavia'), (7, 'El-Salvador'),
					 (37, 'Trinadad&Tobago'), (28, 'Peru'), (16, 'Hong'), (14, 'Holand-Netherlands') 
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
		
		age_value = int(form.age.data)
		fnlwgt_value = int(form.fnlwgt.data)
		education_num_value = int(form.education_num.data)
		capital_gain_value = int(form.capital_gain.data)
		capital_loss_value = int(form.capital_loss.data)
		hours_per_week_value = int(form.hours_per_week.data)

		workclass_value = workclass_choices[int(form.workclass.data)-1][0]
		education_value = education_choices[int(form.education.data)-1][0]
		marital_status_value = marital_choices[int(form.marital_status.data)-1][0]
		occupation_value = occupation_choices[int(form.occupation.data)-1][0]
		relationship_value = relationship_choices[int(form.relationship.data)-1][0]
		race_value = race_choices[int(form.race.data)-1][0]
		sex_value = sex_choices[int(form.sex.data)-1][0]
		native_country_value = native_country_choices[int(form.native_country.data)-1][0]

		model = joblib.load('model_income.pkl')
		value = [age_value, workclass_value, education_value,
				marital_status_value, occupation_value,
				relationship_value, race_value, sex_value, capital_gain_value,
				capital_loss_value, native_country_value
				]
		print('value')
		value = np.array(value).reshape(1,-1)   

		print(value)
		# output income
		result = model.predict(value)
		
		if (result[0] == 0) :
			flash('<= 50K')
		else:
			flash('> 50K')

		return redirect('/')
	return render_template('index.html', form=form)

if __name__ == '__main__':
	app.secret_key = 'The-Capitalist'
	app.run() 