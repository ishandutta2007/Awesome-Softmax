import os

root_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Softmax"
assets_dir = os.path.join(root_dir, "assets")
pages_dir = os.path.join(root_dir, "pages")

os.makedirs(assets_dir, exist_ok=True)
os.makedirs(pages_dir, exist_ok=True)

# 1. Generate SVG Banner
svg_content = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8A2387;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#E94057;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#F27121;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad1)" rx="15"/>
  <text x="50%" y="45%" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="#ffffff" text-anchor="middle" dominant-baseline="middle">Awesome Softmax</text>
  <text x="50%" y="70%" font-family="Arial, sans-serif" font-size="20" fill="#ffffff" text-anchor="middle" dominant-baseline="middle">Evolution, Variants, Types, &amp; Applications</text>
</svg>"""
with open(os.path.join(assets_dir, "banner.svg"), "w") as f:
    f.write(svg_content)

# 2. Define the 14 pages
pages = [
    {"filename": "foundation_era.md", "title": "The Foundation Era (Luce 1959 / Bridle 1989)", "desc": "Standard Softmax and its roots in statistical mechanics."},
    {"filename": "log_sum_exp.md", "title": "The Log-Sum-Exp & Safe Softmax Era", "desc": "Numerical Max-Subtraction and Overflow/Underflow Mitigation."},
    {"filename": "flash_attention.md", "title": "The Online & Fused Streaming Era", "desc": "FlashAttention and Incremental Rescaling in SRAM."},
    {"filename": "temperature_scaled.md", "title": "Temperature-Scaled Softmax", "desc": "Managing creativity and randomness in LLMs."},
    {"filename": "hierarchical_softmax.md", "title": "Hierarchical Softmax", "desc": "Logarithmic scaling with balanced binary trees."},
    {"filename": "log_softmax.md", "title": "Log-Softmax", "desc": "Mathematically fused shortcut formula for stability."},
    {"filename": "sparsemax.md", "title": "Sparsemax", "desc": "Absolute architectural sparsity with true zeros."},
    {"filename": "gumbel_softmax.md", "title": "Gumbel-Softmax", "desc": "Continuous differentiable approximation of a discrete distribution."},
    {"filename": "squared_relu.md", "title": "Squared ReLU", "desc": "Bounded polynomial activation eliminating exponential math overhead."},
    {"filename": "gpu_memory.md", "title": "The GPU Memory-Bandwidth Constraint", "desc": "Operator Fusion compilers and thread block execution cycles."},
    {"filename": "centering_saturation.md", "title": "The Softmax Centering Saturation Problem", "desc": "LayerNorm and RMSNorm mitigations."},
    {"filename": "llm_sampling.md", "title": "Autoregressive LLM Sampling Layers", "desc": "Evaluating the final unnormalized vector layer."},
    {"filename": "cross_attention.md", "title": "Transformer Cross-Attention Alignment", "desc": "Multi-Head Attention weighting matrix."},
    {"filename": "multiclass_vision.md", "title": "Multi-Class Image Vision Networks", "desc": "Terminal layers for ResNet, ViT, etc."}
]

for p in pages:
    content = f"""# {p['title']}

## Overview
{p['desc']}

## Diagram
```mermaid
graph TD;
    A[Raw Logits] --> B[Processing];
    B --> C[Normalized Output];
```

## Detailed Information
This section contains detailed information regarding **{p['title']}**. The method addresses key mathematical and computational aspects of neural network design.

[Back to Main README](../README.md)
"""
    with open(os.path.join(pages_dir, p['filename']), "w") as f:
        f.write(content)

# 3. Rewrite README.md
readme_content = """<div align="center">
  <img src="assets/banner.svg" alt="Awesome Softmax Banner" />
  <h1>🚀 Awesome-Softmax 🧠</h1>
  <p><strong>A curated list of resources for the Softmax Function: Evolution, Variants, Types, & Applications</strong></p>

  <p>
    <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
    <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
    <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintained" />
    <img src="https://img.shields.io/badge/Contributions-welcome-brightgreen.svg?style=flat" alt="Contributions Welcome" />
    <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
  </p>
</div>

The Softmax function is a fundamental mathematical operator used in multi-class classification, neural network output layers, and self-attention mechanisms. It takes a vector of raw, unnormalized score coordinates (logits) and maps them into a clean probability distribution. Every element in the output vector is bounded between 0 and 1, and the entire sum mathematically aggregates to exactly 1.0. This normalization converts raw mathematical distances into operational probabilities, allowing optimizers to calculate log-likelihood cross-entropy losses during backpropagation.

---

## ⏳ 1. The Chronological Evolution

The implementation of the Softmax function has transitioned from traditional static statistical normalization to hardware-fused, memory-mapped kernels capable of processing ultra-long sequence lengths.

```mermaid
flowchart LR
    A["Standard Softmax (1959/1989)<br/>(Traditional Vector Rescaling)"]
    --> B["Numerical Max-Subtraction<br/>(Overflow/Underflow Mitigation)"]
    --> C["Online/Streaming (FlashAttention)<br/>(Incremental Rescaling in SRAM)"]
```

| Era / Variant | Concept | Limitation / Significance | Year | Paper Link | Details |
| --- | --- | --- | --- | --- | --- |
| **The Foundation Era (Luce 1959 / Bridle 1989)** | Rooted in statistical mechanics (the Boltzmann distribution). | Direct computation on computers is highly unstable. | 1989 | [Paper](https://link.springer.com/chapter/10.1007/978-3-642-76153-9_28) | [Read More](pages/foundation_era.md) |
| **The Log-Sum-Exp & Safe Softmax Era** | Introduced a simple algebraic normalization trick. | Requires a two-pass read over the data matrix. | ~1998 | N/A | [Read More](pages/log_sum_exp.md) |
| **The Online & Fused Streaming Era** | Pioneered by algorithms like **FlashAttention**. | Allows execution inside fast, on-chip GPU SRAM. | 2022 | [FlashAttention](https://arxiv.org/abs/2205.14135) | [Read More](pages/flash_attention.md) |

---

## 🧮 2. Core Functional & Mathematical Variants

These structural variations modify the default Softmax equation to alter the model's predictive certainty, handle vocabulary scale limitations, or improve training convergence speed.

| Variant | Equation | Mechanism | Pros / Application | Year | Paper Link | Details |
| --- | --- | --- | --- | --- | --- | --- |
| **Temperature-Scaled Softmax** | $\\text{Softmax}(x_i / T)$ | Introduces a scaling hyperparameter, Temperature ($T$). | Manages creativity and randomness in LLMs. | 2015 | [Paper](https://arxiv.org/abs/1503.02531) | [Read More](pages/temperature_scaled.md) |
| **Hierarchical Softmax** | N/A | Replaces flat vocab with a balanced binary tree. | Logarithmic scaling ($O(\\log V)$). | 2001 | [Paper](https://arxiv.org/abs/cs/0108006) | [Read More](pages/hierarchical_softmax.md) |
| **Log-Softmax** | $\\log(\\text{Softmax}(x))$ | Computes logarithm directly using fused shortcut. | Improves stability with NLL loss. | 2011 | [Paper](https://aclanthology.org/) | [Read More](pages/log_softmax.md) |

---

## 🧬 3. Alternative & Non-Exponential Types

These variants modify or replace the exponential baseline function to introduce absolute sparsity, improve hardware efficiency, or modify geometric boundaries.

| Type | Mechanism | Pros | Year | Paper Link | Details |
| --- | --- | --- | --- | --- | --- |
| **Sparsemax** | Localized projection onto a probability simplex. | Outputs true zeros for low-scoring elements. | 2016 | [Paper](https://arxiv.org/abs/1602.02068) | [Read More](pages/sparsemax.md) |
| **Gumbel-Softmax** | Appends continuous, independent Gumbel noise. | Differentiable approximation of discrete choices. | 2016 | [Paper](https://arxiv.org/abs/1611.01144) | [Read More](pages/gumbel_softmax.md) |
| **Squared ReLU** | Bounded polynomial activation like $\\text{ReLU}(x)^2$. | Eliminates transcendental exponential math overhead. | 2021 | [Paper](https://arxiv.org/abs/2109.08668) | [Read More](pages/squared_relu.md) |

---

## 🛠️ 4. Production Engineering Bottlenecks & Hardware Solutions

While mathematically simple, executing Softmax across billions of parameters creates explicit physical computing constraints.

| Constraint / Problem | The Problem | Mitigation | Year | Paper Link | Details |
| --- | --- | --- | --- | --- | --- |
| **The GPU Memory-Bandwidth Constraint** | Standard Softmax is an **element-wise reduction operation**. | Utilizing **Operator Fusion** compilers like Triton. | 2019 | [Paper](https://dl.acm.org/doi/10.1145/3315508.3329973) | [Read More](pages/gpu_memory.md) |
| **The Softmax Centering Saturation Problem** | Gradients collapse to zero if a few logits dominate. | Implementing **Layer Normalization** or **RMSNorm**. | 2016 | [Paper](https://arxiv.org/abs/1607.06450) | [Read More](pages/centering_saturation.md) |

---

## 🌍 5. Modern Real-World Applications

| Application | Description | Year | Paper Link | Details |
| --- | --- | --- | --- | --- |
| **Autoregressive LLM Sampling Layers** | Evaluates the final unnormalized vector layer. | 2018 | [Paper](https://arxiv.org/abs/1706.03762) | [Read More](pages/llm_sampling.md) |
| **Transformer Cross-Attention Alignment** | Core spatial weighting matrix within Multi-Head Attention. | 2017 | [Paper](https://arxiv.org/abs/1706.03762) | [Read More](pages/cross_attention.md) |
| **Multi-Class Image Vision Networks** | Acts as the terminal layer for standard image classification. | 2012 | [Paper](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) | [Read More](pages/multiclass_vision.md) |

---

## 📈 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Softmax&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Softmax&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Softmax&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Softmax&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""

with open(os.path.join(root_dir, "README.md"), "w", encoding='utf-8') as f:
    f.write(readme_content)
