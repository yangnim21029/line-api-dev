---
name: line-flex-message
description: Comprehensive guide and toolkit for creating advanced LINE Flex Messages with complex layouts, video integration, and implementing reliable API retry mechanisms with X-Line-Retry-Key. Use when creating sophisticated Bot UIs, handling high-load messaging, or designing robust communication layers for LINE.
---

# LINE Flex Message & Reliability Skill

This skill extends Claude's ability to design high-quality, brand-consistent LINE Flex Messages and implement reliable messaging workflows.

## Core Capabilities

1. **Advanced Flex Layouts**: Precise control over nested boxes, dynamic widths, and complex UI patterns (e.g., flight tickets, product lists).
2. **Video Integration**: Guidelines and templates for embedding video components in the hero block.
3. **Reliable Communication**: Implementing `X-Line-Retry-Key` and exponential backoff strategies to handle 429/5xx errors.

## Workflow Patterns

### 1. Designing a Complex Flex Message
1. **Identify Layout**: Determine if it's a single Bubble or a Carousel.
2. **Component Mapping**: Map UI elements to Flex blocks (Header, Hero, Body, Footer).
3. **Refine Nesting**: Use `scripts/flex_builder.py` or reference `references/flex-elements.md` to create multi-layer box nesting.
4. **Add Actionability**: Ensure all buttons and images have correct `action` definitions.

### 2. Implementing API Retries
1. **Generate Key**: Use `scripts/flex_builder.py` to generate a unique `X-Line-Retry-Key`.
2. **Header Injection**: Always include the retry key in the first request for supported APIs (Push, Multicast, etc.).
3. **Error Handling**: Follow the decision matrix in `references/retry-policy.md`:
   - **429/5xx/Timeout**: Retry with exponential backoff.
   - **409**: Log as "already accepted" and proceed.
   - **2xx**: Success.

## Resources

- **[Flex Elements & Layout Guide](references/flex-elements.md)**: Detailed component specifications.
- **[Flex Video Guide](references/video-flex.md)**: Requirements and examples for video embedding.
- **[Retry & Reliability Policy](references/retry-policy.md)**: Strategic guide for headers and error handling.
- **[Flex Builder Script](scripts/flex_builder.py)**: Python utility for generating complex Flex JSON and retry headers.

## Layout Patterns Examples

- **Product List**: Use nested horizontal boxes for image + text rows.
- **Video Hero**: Mega/Giga sized bubbles with `type: video` in hero block.
- **Carousel**: Side-scrolling bubbles for browsing multiple items.

## Quality Standards
- **Consistency**: Use `spacing` and `margin` consistently across bubbles.
- **Responsiveness**: Use `wrap: true` for text and test layouts with different font sizes.
- **Stability**: Never send high-frequency messages without a retry strategy.
