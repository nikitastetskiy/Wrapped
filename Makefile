PROJECTNAME := wrapper

build: ## Build the project
	@echo "Building..."
	docker-compose build wrapper
up: ## Run the container
	@echo "Starting..."
	docker-compose up -d
shell: ## Runs a shell in the container
	@echo "Opening shell..."
	docker-compose exec wrapper bash