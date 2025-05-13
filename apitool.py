import requests

# Azure API details
subscription_id = "your-subscription-id"
resource_group = "example-resource-group"
account_name = "example-anf-account"
capacity_pool = "example-capacity-pool"
volume_name = "example-volume"
location = "eastus"
cifs_user = "example-user"
cifs_password = "example-password"

# Azure authentication
tenant_id = "your-tenant-id"
client_id = "your-client-id"
client_secret = "your-client-secret"
auth_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"

auth_payload = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "resource": "https://management.azure.com/"
}

auth_response = requests.post(auth_url, data=auth_payload)
auth_response.raise_for_status()
access_token = auth_response.json()["access_token"]

# Define headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Create CIFS volume
volume_url = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{capacity_pool}/volumes/{volume_name}?api-version=2023-09-01"

volume_payload = {
    "location": location,
    "properties": {
        "creationToken": volume_name,
        "usageThreshold": 100 * 1024 * 1024 * 1024,  # 100GB in bytes
        "serviceLevel": "Premium",
        "protocolTypes": ["CIFS"],
        "subnetId": "/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Network/virtualNetworks/example-vnet/subnets/example-subnet",
        "securityStyle": "ntfs",
        "cifs": {
            "smbAccessBasedEnumeration": True,
            "smbContinuouslyAvailable": True,
            "smbEncryption": True
        }
    }
}

volume_response = requests.put(volume_url, json=volume_payload, headers=headers)
volume_response.raise_for_status()

print("CIFS volume created successfully!")
