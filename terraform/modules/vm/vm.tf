resource "azurerm_network_interface" "NI" {
  name                = "NI"
  location            = var.location
  resource_group_name = var.resource_group

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id_test
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip_address_id
  }
}

resource "azurerm_linux_virtual_machine" "VM" {
  name                  = "Vm2"
  location              = var.location
  resource_group_name   = var.resource_group
  size                  = "Standard_DS2_v2"
  admin_username        = var.admin_user
  admin_password        = var.admin_password
  network_interface_ids = [azurerm_network_interface.NI.id]
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_id = var.source_image_id
  # source_image_reference {
  #   publisher = "Canonical"
  #   offer     = "UbuntuServer"
  #   sku       = "18.04-LTS"
  #   version   = "latest"
  # }
}
