

# Multiple Providers

  

You can use multiple providers in one single terraform project. For example,

  
  

1. Create a providers.tf file in the root directory of your Terraform project.

2. In the providers.tf file, define the AWS and Azure providers. For example:

  
  

```

provider "aws" {

  region = "us-east-1"

}

  

provider "azurerm" {

  subscription_id = "your-azure-subscription-id"

  client_id = "your-azure-client-id"

  client_secret = "your-azure-client-secret"

  tenant_id = "your-azure-tenant-id"

}

```

  

3. In your other Terraform configuration files, you can then use the aws and azurerm providers to create resources in AWS and Azure, respectively,

  

```

resource "aws_instance" "example" {

  ami = "ami-0123456789abcdef0"

  instance_type = "t2.micro"

}

  

resource "azurerm_virtual_machine" "example" {

  name = "example-vm"

  location = "eastus"

  size = "Standard_A1"

}

```


# Multiple Region Implementation in Terraform

  

You can make use of `alias` keyword to implement multi region infrastructure setup in

terraform.

  

```

provider "aws" {

  alias = "us-east-1"

  region = "us-east-1"

}

  

provider "aws" {

  alias = "us-west-2"

  region = "us-west-2"

}

  

resource "aws_instance" "example" {

  ami = "ami-0123456789abcdef0"

  instance_type = "t2.micro"

  provider = "aws.us-east-1"

}

  

resource "aws_instance" "example2" {

  ami = "ami-0123456789abcdef0"

  instance_type = "t2.micro"

  provider = "aws.us-west-2"

}

```

# Provider Configuration

  

The required_providers block in Terraform is used to declare and specify the required provider configurations for your Terraform module or configuration. It allows you to specify the provider name, source, and version constraints.

  

```

terraform {

  required_providers {

    aws = {

      source  = "hashicorp/aws"

      version = "~> 3.0"

    }

    azurerm = {

      source  = "hashicorp/azurerm"

      version = ">= 2.0, < 3.0"

    }

  }

}

```

# Variables

  

Input and output variables in Terraform are essential for parameterizing and sharing values within your Terraform configurations and modules. They allow you to make your configurations more dynamic, reusable, and flexible.

  

## Input Variables

  

Input variables are used to parameterize your Terraform configurations. They allow you to pass values into your modules or configurations from the outside. Input variables can be defined within a module or at the root level of your configuration. Here's how you define an input variable:

  

```hcl

variable "example_var" {

  description = "An example input variable"

  type        = string

  default     = "default_value"

}

```

  

In this example:

  

- `variable` is used to declare an input variable named `example_var`.

- `description` provides a human-readable description of the variable.

- `type` specifies the data type of the variable (e.g., `string`, `number`, `list`, `map`, etc.).

- `default` provides a default value for the variable, which is optional.

  

You can then use the input variable within your module or configuration like this:

  

```hcl

resource "example_resource" "example" {

  name = var.example_var

  # other resource configurations

}

```

  

You reference the input variable using `var.example_var`.

  

## Output Variables

  

Output variables allow you to expose values from your module or configuration, making them available for use in other parts of your Terraform setup. Here's how you define an output variable:

  

```hcl

output "example_output" {

  description = "An example output variable"

  value       = resource.example_resource.example.id

}

```

  

In this example:

  

- `output` is used to declare an output variable named `example_output`.

- `description` provides a description of the output variable.

- `value` specifies the value that you want to expose as an output variable. This value can be a resource attribute, a computed value, or any other expression.

  

You can reference output variables in the root module or in other modules by using the syntax `module.module_name.output_name`, where `module_name` is the name of the module containing the output variable.

  

For example, if you have an output variable named `example_output` in a module called `example_module`, you can access it in the root module like this:

  

```hcl

output "root_output" {

  value = module.example_module.example_output

}

```

  

This allows you to share data and values between different parts of your Terraform configuration and create more modular and maintainable infrastructure-as-code setups.

# Terraform tfvars

  

In Terraform, `.tfvars` files (typically with a `.tfvars` extension) are used to set specific values for input variables defined in your Terraform configuration.

  

They allow you to separate configuration values from your Terraform code, making it easier to manage different configurations for different environments (e.g., development, staging, production) or to store sensitive information without exposing it in your code.

  

Here's the purpose of `.tfvars` files:

  

1. **Separation of Configuration from Code**: Input variables in Terraform are meant to be configurable so that you can use the same code with different sets of values. Instead of hardcoding these values directly into your `.tf` files, you use `.tfvars` files to keep the configuration separate. This makes it easier to maintain and manage configurations for different environments.

  

2. **Sensitive Information**: `.tfvars` files are a common place to store sensitive information like API keys, access credentials, or secrets. These sensitive values can be kept outside the version control system, enhancing security and preventing accidental exposure of secrets in your codebase.

  

3. **Reusability**: By keeping configuration values in separate `.tfvars` files, you can reuse the same Terraform code with different sets of variables. This is useful for creating infrastructure for different projects or environments using a single set of Terraform modules.

  

4. **Collaboration**: When working in a team, each team member can have their own `.tfvars` file to set values specific to their environment or workflow. This avoids conflicts in the codebase when multiple people are working on the same Terraform project.

  

## Summary

  

Here's how you typically use `.tfvars` files

  

1. Define your input variables in your Terraform code (e.g., in a `variables.tf` file).

  

2. Create one or more `.tfvars` files, each containing specific values for those input variables.

  

3. When running Terraform commands (e.g., terraform apply, terraform plan), you can specify which .tfvars file(s) to use with the -var-file option:

  

```

terraform apply -var-file=dev.tfvars

```

  

By using `.tfvars` files, you can keep your Terraform code more generic and flexible while tailoring configurations to different scenarios and environments.

# Conditional Expressions

  

Conditional expressions in Terraform are used to define conditional logic within your configurations. They allow you to make decisions or set values based on conditions. Conditional expressions are typically used to control whether resources are created or configured based on the evaluation of a condition.

  

The syntax for a conditional expression in Terraform is:

  

```hcl

condition ? true_val : false_val

```

  

- `condition` is an expression that evaluates to either `true` or `false`.

- `true_val` is the value that is returned if the condition is `true`.

- `false_val` is the value that is returned if the condition is `false`.

  

Here are some common use cases and examples of how to use conditional expressions in Terraform:

  

## Conditional Resource Creation Example

  

```hcl

resource "aws_instance" "example" {

  count = var.create_instance ? 1 : 0

  

  ami           = "ami-XXXXXXXXXXXXXXXXX"

  instance_type = "t2.micro"

}

```

  

In this example, the `count` attribute of the `aws_instance` resource uses a conditional expression. If the `create_instance` variable is `true`, it creates one EC2 instance. If `create_instance` is `false`, it creates zero instances, effectively skipping resource creation.

  

# Conditional Variable Assignment Example

  

```hcl

variable "environment" {

  description = "Environment type"

  type        = string

  default     = "development"

}

  

variable "production_subnet_cidr" {

  description = "CIDR block for production subnet"

  type        = string

  default     = "10.0.1.0/24"

}

  

variable "development_subnet_cidr" {

  description = "CIDR block for development subnet"

  type        = string

  default     = "10.0.2.0/24"

}

  

resource "aws_security_group" "example" {

  name        = "example-sg"

  description = "Example security group"

  

  ingress {

    from_port   = 22

    to_port     = 22

    protocol    = "tcp"

    cidr_blocks = var.environment == "production" ? [var.production_subnet_cidr] : [var.development_subnet_cidr]

  }

}

  

```

  

In this example, the `locals` block uses a conditional expression to assign a value to the `subnet_cidr` local variable based on the value of the `environment` variable. If `environment` is set to `"production"`, it uses the `production_subnet_cidr` variable; otherwise, it uses the `development_subnet_cidr` variable.

  

## Conditional Resource Configuration

  

```hcl

resource "aws_security_group" "example" {

  name = "example-sg"

  description = "Example security group"

  

  ingress {

    from_port   = 22

    to_port     = 22

    protocol    = "tcp"

    cidr_blocks = var.enable_ssh ? ["0.0.0.0/0"] : []

  }

}

```

  

In this example, the `ingress` block within the `aws_security_group` resource uses a conditional expression to control whether SSH access is allowed. If `enable_ssh` is `true`, it allows SSH traffic from any source (`"0.0.0.0/0"`); otherwise, it allows no inbound traffic.

  

Conditional expressions in Terraform provide a powerful way to make decisions and customize your infrastructure deployments based on various conditions and variables. They enhance the flexibility and reusability of your Terraform configurations.