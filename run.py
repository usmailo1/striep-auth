from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/id=<id>', methods=['GET'])
def stripe_auth(id):
    data = f'source={id}&browser=%7B%22fingerprintAttempted%22%3Afalse%2C%22fingerprintData%22%3Anull%2C%22challengeWindowSize%22%3Anull%2C%22threeDSCompInd%22%3A%22Y%22%2C%22browserJavaEnabled%22%3Afalse%2C%22browserJavascriptEnabled%22%3Atrue%2C%22browserLanguage%22%3A%22en-US%22%2C%22browserColorDepth%22%3A%2224%22%2C%22browserScreenHeight%22%3A%221080%22%2C%22browserScreenWidth%22%3A%221920%22%2C%22browserTZ%22%3A%22-300%22%2C%22browserUserAgent%22%3A%22Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F125.0.0.0+Safari%2F537.36%22%7D&one_click_authn_device_support[hosted]=false&one_click_authn_device_support[same_origin_frame]=false&one_click_authn_device_support[spc_eligible]=true&one_click_authn_device_support[webauthn_eligible]=true&one_click_authn_device_support[publickey_credentials_get_allowed]=true&key=pk_live_51Kdt7SITYN3XHFYv04oDDWHUzrayh00tQBDaoaiLZyjJc40lWT7Sr14iXdM7aVMN8NPg35bvDRos5QhfNeouIvTC00EbAy1MUw'
    
    resp = requests.post('https://api.stripe.com/v1/3ds2/authenticate', data=data)
    return jsonify(resp.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

