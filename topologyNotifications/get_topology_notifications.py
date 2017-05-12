import azurerm
import sys

access_token = azurerm.get_access_token(
    sys.argv[1],
    sys.argv[2],
    sys.argv[3]
)

print(access_token)
