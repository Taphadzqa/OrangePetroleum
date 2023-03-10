from flask import render_template, Blueprint


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    return render_template('main/home.html', title='Welcome')


@main.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('main/about.html', title='About us')


@main.route('/products_and_services', methods=['GET', 'POST'])
def services():
    return render_template('main/services.html', title='Products/Services')


@main.route('/partnerships', methods=['GET', 'POST'])
def partnerships():
    return render_template('main/partnerships.html', title='Partnerships')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('main/contact.html', title='Contact us')
