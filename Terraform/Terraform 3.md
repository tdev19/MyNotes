# Built-in Functions

  

Terraform is an infrastructure as code (IaC) tool that allows you to define and provision infrastructure resources in a declarative manner. Terraform provides a wide range of built-in functions that you can use within your configuration files (usually written in HashiCorp Configuration Language, or HCL) to manipulate and transform data. These functions help you perform various tasks when defining your infrastructure. Here are some commonly used built-in functions in Terraform:

  

1. `concat(list1, list2, ...)`: Combines multiple lists into a single list.

  

```hcl

variable "list1" {

  type    = list

  default = ["a", "b"]

}

  

variable "list2" {

  type    = list

  default = ["c", "d"]

}

  

output "combined_list" {

  value = concat(var.list1, var.list2)

}

```

  

2. `element(list, index)`: Returns the element at the specified index in a list.

  

```hcl

variable "my_list" {

  type    = list

  default = ["apple", "banana", "cherry"]

}

  

output "selected_element" {

  value = element(var.my_list, 1) # Returns "banana"

}

```

  

3. `length(list)`: Returns the number of elements in a list.

  

```hcl

variable "my_list" {

  type    = list

  default = ["apple", "banana", "cherry"]

}

  

output "list_length" {

  value = length(var.my_list) # Returns 3

}

```

  

4. `map(key, value)`: Creates a map from a list of keys and a list of values.

  

```hcl

variable "keys" {

  type    = list

  default = ["name", "age"]

}

  

variable "values" {

  type    = list

  default = ["Alice", 30]

}

  

output "my_map" {

  value = map(var.keys, var.values) # Returns {"name" = "Alice", "age" = 30}

}

```

  

5. `lookup(map, key)`: Retrieves the value associated with a specific key in a map.

  

```hcl

variable "my_map" {

  type    = map(string)

  default = {"name" = "Alice", "age" = "30"}

}

  

output "value" {

  value = lookup(var.my_map, "name") # Returns "Alice"

}

```

  

6. `join(separator, list)`: Joins the elements of a list into a single string using the specified separator.

  

```hcl

variable "my_list" {

  type    = list

  default = ["apple", "banana", "cherry"]

}

  

output "joined_string" {

  value = join(", ", var.my_list) # Returns "apple, banana, cherry"

}

```

  

These are just a few examples of the built-in functions available in Terraform. You can find more functions and detailed documentation in the official Terraform documentation, which is regularly updated to include new features and improvements

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