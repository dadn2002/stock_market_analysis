import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
ecom_line = ecom_sales.groupby(['Year-Month','Country'])['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
ecom_bar = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
line_graph = px.line(data_frame=ecom_line, x='Year-Month', y='Total Sales ($)', title='Total Sales by Month', color='Country')
bar_graph = px.bar(data_frame=ecom_bar, x='Total Sales ($)', y='Country', orientation='h',title='Total Sales by Country')

# Create the Dash app
app = dash.Dash(__name__)

# Set up the layout using an overall div
app.layout = html.Div(
    children=[
  # Add a H1
  html.H1("Sales by Country & Over Time"),
  # Add both graphs
  dcc.Graph(id='line_graph', figure=line_graph),
  dcc.Graph(id='bar_graph', figure=bar_graph)
  ])

if __name__ == '__main__':
    app.run_server(debug=True)



ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
ecom_line = ecom_sales.groupby('Year-Month')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
line_fig = px.line(data_frame=ecom_line, x='Year-Month', y='Total Sales ($)', title='Total Sales by Month')
ecom_bar = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
max_country = ecom_bar.sort_values(by='Total Sales ($)', ascending=False).loc[0]['Country']
bar_fig = px.bar(data_frame=ecom_bar, x='Total Sales ($)', y='Country', orientation='h', title='Total Sales by Country')

app = dash.Dash(__name__)

# Create the dash layout and overall div
app.layout = html.Div(children=[
    html.H1('Sales Figures'), 
    # Add a div containing the line figure
    html.Div(dcc.Graph(id='my-line-fig', figure=line_fig)), 
    # Add a div containing the bar figure
    html.Div(dcc.Graph(id='my-bar-fig', figure=bar_fig)), 
    # Add the H3
    html.H3(f'The largest country by sales was {max_country}')
    ])

if __name__ == '__main__':
    app.run_server(debug=True)


    ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
ecom_sales = ecom_sales.groupby(['Year-Month','Country'])['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')

# Create the line graph
line_graph = px.line(
  # Set the appropriate DataFrame and title
  data_frame=ecom_sales, title="Total Sales by Country and Month", 
  # Set the x and y arguments
  x='Year-Month', y='Total Sales ($)',
  # Ensure a separate line per country
  color='Country')

line_graph.show()


ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
ecom_sales = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')

# Create the bar graph object
bar_fig = px.bar(
  # Set the DataFrame, x and y
  data_frame=ecom_sales, x='Total Sales ($)', y='Country',
  # Set the graph to be horizontal
  orientation='h', title='Total Sales by Country')

# Increase the gap between bars
bar_fig.update_layout({'bargap': 0.5})

bar_fig.show()


ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/2bac9433b0e904735feefa26ca913fba187c0d55/e_com_logo.png'
ecom_bar = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)').sort_values(by='Total Sales ($)', ascending=False)
top_country = ecom_bar.loc[0]['Country']            
bar_fig_country = px.bar(ecom_bar, x='Total Sales ($)', y='Country', color='Country', color_discrete_map={'United Kingdom':'lightblue', 'Germany':'orange', 'France':'darkblue', 'Australia':'green', 'Hong Kong':'red'})         
    
app = dash.Dash(__name__)

app.layout = html.Div([
  # Add the company logo
  html.Img(src=logo_link),
  html.H1('Sales by Country'),
  html.Div(dcc.Graph(figure=bar_fig_country), 
           style={'width':'750px', 'margin':'auto'}),
  # Add an overall text-containing component
  html.Span(children=[
    # Add the top country text
    'This year, the most sales came from: ', 
    html.B(top_country),
    # Italicize copyright notice
    html.I(' Copyright E-Com INC')])
    ], 
  style={'text-align':'center', 'font-size':22})

if __name__ == '__main__':
    app.run_server(debug=True)


ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/2bac9433b0e904735feefa26ca913fba187c0d55/e_com_logo.png'
ecom_category = ecom_sales.groupby(['Major Category','Minor Category']).size().reset_index(name='Total Orders').sort_values(by='Total Orders', ascending=False).reset_index(drop=True)
num1_cat, num1_salesvol = ecom_category.loc[0].tolist()[1:3]
num2_cat, num2_salesvol = ecom_category.loc[1].tolist()[1:3]
ecom_bar = px.bar(ecom_category, x='Total Orders', y='Minor Category', color='Major Category')
ecom_bar.update_layout({'yaxis':{'dtick':1, 'categoryorder':'total ascending'}})             

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Img(src=logo_link),
    html.H1('Top Sales Categories'),
    html.Div(dcc.Graph(figure=ecom_bar)),
    html.Span(children=[
    'The top 2 sales categories were:',
    # Set up an ordered list
    html.Ol(children=[
      	# Add two list elements with the top category variables
        html.Li(children=[num1_cat, ' with ', num1_salesvol, ' sales volume']),
        html.Li(children=[num2_cat, ' with ', num2_salesvol, ' sales volume'])
    ], style={'width':'350px', 'margin':'auto'}),
    # Add a line break before the copyright notice
    html.Br(),
    html.I('Copyright E-Com INC')])
    ], style={'text-align':'center', 'font-size':22})

if __name__ == '__main__':
    app.run_server(debug=True)


ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'

app = dash.Dash(__name__)

app.layout = html.Div([
  html.Img(src=logo_link,style={'margin':'30px 0px 0px 0px' }),
  html.H1('Sales breakdowns'),
  html.Div(
    children=[
    html.Div(
        children=[
        html.H2('Controls'),
        html.Br(),
        html.H3('Country Select'),
        # Add a dropdown with identifier
        dcc.Dropdown(id='country_dd',
        # Set the available options with noted labels and values
        options=[
            {'label':'UK', 'value':'United Kingdom'},
            {'label':'GM', 'value':'Germany'},
            {'label':'FR', 'value':'France'},
            {'label':'AUS', 'value':'Australia'},
            {'label':'HK', 'value':'Hong Kong'}],
            style={'width':'200px', 'margin':'0 auto'})
        ],
        style={'width':'350px', 'height':'350px', 'display':'inline-block', 'vertical-align':'top', 'border':'1px solid black', 'padding':'20px'}),
    html.Div(children=[
            # Add a graph component with identifier
            dcc.Graph(id='major_cat'),
            html.H2('Major Category', 
            style={ 'border':'2px solid black', 'width':'200px', 'margin':'0 auto'})
            ],
             style={'width':'700px','display':'inline-block'}
             ),
    ])], 
  style={'text-align':'center', 'display':'inline-block', 'width':'100%'}
  )

@app.callback(
    # Set the input and output of the callback to link the dropdown to the graph
    Output(component_id='major_cat', component_property='figure'),
    Input(component_id='country_dd', component_property='value')
)

def update_plot(input_country):
    country_filter = 'All Countries'
    sales = ecom_sales.copy(deep=True)
    if input_country:
        country_filter = input_country
        sales = sales[sales['Country'] == country_filter]
    ecom_bar_major_cat = sales.groupby('Major Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
    bar_fig_major_cat = px.bar(
        title=f'Sales in {country_filter}', data_frame=ecom_bar_major_cat, x='Total Sales ($)', y='Major Category', color='Major Category',
                 color_discrete_map={'Clothes':'blue','Kitchen':'red','Garden':'green','Household':'yellow'})
    return bar_fig_major_cat


if __name__ == '__main__':
    app.run_server(debug=True)


import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from datetime import datetime, date
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'
ecom_sales['InvoiceDate'] = pd.to_datetime(ecom_sales['InvoiceDate'])

app = dash.Dash(__name__)

app.layout = html.Div([
  html.Img(src=logo_link, 
        style={'margin':'30px 0px 0px 0px' }),
  html.H1('Sales breakdowns'),
  html.Div(
    children=[
    html.Div(
        children=[
        html.H2('Controls'),
        html.Br(),
        html.H3('Sale Date Select'),
        # Create a single date picker with identifier
        dcc.DatePickerSingle(id='sale_date',
            # Set the min/max dates allowed as the min/max dates in the DataFrame
            min_date_allowed=ecom_sales['InvoiceDate'].min(),
            max_date_allowed=ecom_sales['InvoiceDate'].max(),
            # Set the initial visible date
            date=date(2011,4,11),
            initial_visible_month=date(2011,4,11),
            style={'width':'200px', 'margin':'0 auto'})
        ],
        style={'width':'350px', 'height':'350px', 'display':'inline-block', 'vertical-align':'top', 'border':'1px solid black', 'padding':'20px'}),
    html.Div(children=[
      		# Add a component to render a Plotly figure with the specified id
            dcc.Graph('sales_cat'),
            html.H2('Daily Sales by Major Category', 
            style={ 'border':'2px solid black', 'width':'400px', 'margin':'0 auto'})
            ],
             style={'width':'700px','display':'inline-block'}
             ),
    ]),
    ], 
  style={'text-align':'center', 'display':'inline-block', 'width':'100%'}
  )

@app.callback(
    Output(component_id='sales_cat', component_property='figure'),
    Input(component_id='sale_date', component_property='date')
)
def update_plot(input_date):
    
    sales = ecom_sales.copy(deep=True)
    if input_date:
        sales = sales[sales['InvoiceDate'] == input_date]
        
    ecom_bar_major_cat = sales.groupby('Major Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
    bar_fig_major_cat = px.bar(
        title=f'Sales on: {input_date}',data_frame=ecom_bar_major_cat, orientation='h', 
        x='Total Sales ($)', y='Major Category')

    return bar_fig_major_cat


if __name__ == '__main__':
    app.run_server(debug=True)


