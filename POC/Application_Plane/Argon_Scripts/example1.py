import requests
import json

def get_odl_controller_status(ip, port=8181, username='admin', password='admin'):
    """
    Function to get the status of the ODL controller.
    :param ip: IP address of the ODL controller.
    :param port: Port number (default is 8181).
    :param username: Username for ODL controller.
    :param password: Password for ODL controller.
    :return: Status of the ODL controller.
    """
    url = f"http://{ip}:{port}/restconf/operational/network-topology:network-topology/topology/flow:1"
    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers, auth=(username, password))

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    controller_ip = "192.168.16.128"  # Replace with your controller IP
    status = get_odl_controller_status(controller_ip)
    print("ODL Controller Status:", status)
