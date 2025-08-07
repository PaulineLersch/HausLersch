# Overview

This project is a single-page website for "Haus Lersch," a German restaurant group operating three dining locations. The website serves as a central hub showcasing all locations: Seehaus 53, Äu's Gasthaus, and Almhütte (a seasonal winter location). The site features a modern, responsive design with smooth scrolling navigation between sections for each restaurant location, reservation integration, and downloadable resources like menus and banquet information.

# User Preferences

Preferred communication style: Simple, everyday language.
Project preference: Remove all Indemann 1 references completely (confirmed removed August 2025).

# System Architecture

## Frontend Architecture
- **Single-page application (SPA)**: All content, styles, and functionality contained within a single `index.html` file
- **CSS-in-HTML approach**: All styling embedded using `<style>` tags for simplified deployment
- **Vanilla JavaScript**: No external frameworks, keeping the solution lightweight and fast-loading
- **Mobile-first responsive design**: Optimized for mobile devices with desktop enhancements

## Design System
- **CSS Custom Properties**: Centralized color scheme using CSS variables for consistent branding across locations
- **Location-specific color coding**: Each restaurant has a unique brand color (#662481 for Seehaus 53, #a31e23 for Äu's Gasthaus, #662481 for Almhütte)
- **Fixed navigation**: Sticky header with smooth scrolling to sections
- **Card-based layout**: Each location presented in dedicated sections with hero images and action buttons

## Content Structure
- **Hero section**: Main landing area with logo and overview of all locations
- **Location sections**: Individual sections for each restaurant with descriptions, images, and call-to-action buttons
- **Resource integration**: PDF downloads for menus and banquet information
- **Reservation system**: Integration with external reservation platform (dish.co)

## Navigation System
- **Smooth scroll implementation**: JavaScript-powered navigation between sections
- **Fixed header**: Always-visible navigation bar with backdrop blur effect
- **Section-based routing**: Internal anchors for direct linking to specific locations

# External Dependencies

## Reservation System
- **dish.co integration**: Third-party reservation widgets embedded via iframes
- **Location-specific reservation URLs**: Each restaurant has unique reservation endpoints
- Seehaus 53: `hydra-d9c16acf-0310-4d3d-9f5f-061441b0a117`

- Äu's Gasthaus: `hydra-ee475637-cfe9-4b3b-8d0d-0d96150cb066`

## Static Assets
- **Hero images**: Location-specific images (seehaus-hero.jpg, aeusgasthaus-hero.jpg, almhuette-hero.jpg)
- **PDF resources**: Downloadable menus and banquet information for each location
- **Logo assets**: Main Haus Lersch branding materials

## Typography and Fonts
- **System fonts**: Utilizes native font stack (-apple-system, BlinkMacSystemFont, Segoe UI, Roboto) for optimal performance
- **Serif headings**: Georgia/Times New Roman for elegant headings

## Browser APIs
- **Smooth scrolling**: CSS and JavaScript scroll behavior for enhanced user experience
- **Backdrop filter**: Modern CSS effects for navigation transparency
- **Responsive design**: CSS Grid and Flexbox for adaptive layouts