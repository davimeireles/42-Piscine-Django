from django.shortcuts import render
# Create your views here.


def hex_color(base_rgb, factor):
    return '#{:02x}{:02x}{:02x}'.format(
        int(base_rgb[0] * factor),
        int(base_rgb[1] * factor),
        int(base_rgb[2] * factor)
    )

def draw_table(request):
    column_names = ['Noir', 'Rouge', 'Bleu', 'Vert']
    
    base_colors = {
        'Noir': (0,0,0),
        'Rouge': (255,0,0),
        'Bleu': (0,0,255),
        'Vert': (0,255,0),
    }

    rows = []

    # Create 50 shades per color
    for i in range(50):
        factor = (i + 1) / 50 # Gradual from 0.02 to 1.0
        row = []
        for name in column_names:
            color = hex_color(base_colors[name], factor)
            row.append({ 'bg':color })
        rows.append(row)
    
    return render(request, 'table.html', {
        'headers': column_names,
        'rows': rows,
    })