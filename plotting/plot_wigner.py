import numpy as np
import plotly.graph_objects as go

def plot_wigner_plotly(samples, P, N, L, j=0):
    x_j, p_j = samples[:, j], samples[:, j + N]
    limit = np.percentile(np.abs(np.concatenate([x_j, p_j])), 98)
    
    hist, xedges, yedges = np.histogram2d(x_j, p_j, bins=70, weights=P, range=[[-limit, limit], [-limit, limit]], density=True)
    fig = go.Figure(data=[go.Surface(z=hist.T, x=xedges, y=yedges, colorscale='RdBu', cmid=0)])

    fig.update_layout(
        title=f'Interactive Wigner Function (L={L})',
        scene=dict(
            xaxis_title='x',
            yaxis_title='p',
            zaxis_title='W(x,p)'
        ),
        autosize=False, width=900, height=800
    )
    
    fig.write_html(f"results/interactive_wigner_L{L}.html")
    print(f"Interactive plot saved to results/interactive_wigner_L{L}.html - Open this file in your browser!")
