# Flex Message Elements & Layout Guide

Flex Messages consist of three hierarchical levels: **Containers**, **Blocks**, and **Components**.

## 1. Containers
Containers are the top-level building blocks.
- **Bubble**: A single message bubble.
- **Carousel**: Multiple bubbles laid out side-by-side (sideways scrolling).

## 2. Blocks
Units that compose a bubble. Placement order: Header -> Hero -> Body -> Footer.
- **Header**: Subject or title.
- **Hero**: Main image or video.
- **Body**: Main message content.
- **Footer**: Buttons and supplementary info.

## 3. Components
Units that compose a block.
- **Box**: Defines horizontal/vertical layout. Can contain other components (including nested boxes).
- **Button**: Performs an action when tapped (primary, secondary, link styles).
- **Image**: Renders an image (size, aspect ratio, etc.).
- **Video**: Renders a video (specific hero block placement recommended).
- **Icon**: Small decorative icons.
- **Text**: Text strings with style options (font color, size, weight).
- **Span**: Multiple text strings with different styles in one line.
- **Separator**: Horizontal or vertical line.

## 4. Advanced Layout Patterns
### Nested Boxes
Use `box` with `layout: horizontal` or `vertical` to create complex grids.
- `spacing`: Space between components.
- `margin`: Margin before the box.
- `flex`: Proportion of space occupied.

### Dynamic Width & Alignment
- `justifyContent`: For box alignment (center, flex-start, flex-end, space-between, space-around).
- `alignItems`: Alignment within the box.
