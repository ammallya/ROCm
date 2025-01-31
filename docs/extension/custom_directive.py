from docutils.parsers.rst import Directive
import requests

class RemoteIncludeDirective(Directive):
    """Custom directive to fetch and include an RST file from an external repo, parsing it properly."""
    required_arguments = 1  # The URL to fetch

    def run(self):
        url = self.arguments[0]  # Get the provided URL
        try:
            response = requests.get(url)
            response.raise_for_status()
            content = response.text  # Get the file content
        except requests.RequestException as e:
            error_message = f".. Warning:: Failed to fetch content from {url}. Error: {e}"
            return [self.state_machine.reporter.warning(error_message, line=self.lineno)]

        # Insert the fetched content as if it were written in the document
        self.state_machine.insert_input(content.splitlines(), url)
        return []

# Register the directive
def setup(app):
    app.add_directive("include_remote", RemoteIncludeDirective)
