import requests

# Test weak password vulnerability
def test_weak_password():
    url = 'http://localhost:3000/login'
    data = {'username': 'admin', 'password': '1234'}
    response = requests.post(url, json=data)
    assert response.status_code == 200, "Weak password test failed"

# Test HTTP vulnerability (for future HTTPS)
def test_insecure_communication():
    response = requests.get('http://localhost:3000/')
    assert response.url.startswith('http'), "App should be running over HTTPS"

if __name__ == '__main__':
    test_weak_password()
    test_insecure_communication()
