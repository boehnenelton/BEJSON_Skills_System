# BECSS Component Template (Python)

def html_component(title, content, variant=None):
    \"\"\"
    Standard BECSS component generator.
    Follows BEM (c-prefix) and zero-inline-style mandate.
    \"\"\"
    modifier = f" c-component--{variant}" if variant else ""
    
    return f\"\"\"
    <article class="c-component{modifier}">
        <header class="c-component__header">
            <h3 class="c-component__title">{{title}}</h3>
        </header>
        <div class="c-component__body">
            {{content}}
        </div>
    </article>
    \"\"\"
