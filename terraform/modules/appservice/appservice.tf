resource "azurerm_service_plan" "test" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = var.location
  resource_group_name = var.resource_group
  os_type             = "Linux"
  sku_name            = "F1"
}

resource "azurerm_windows_web_app" "test" {
  name                = var.application_name
  location            = var.location
  resource_group_name = var.resource_group

  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE" = 0
  }

  site_config {
    always_on = false
    application_stack {
      dotnet_version = "v6.0"
      current_stack = "dotnetcore"
    }
  }

  service_plan_id = azurerm_service_plan.test.id
}
