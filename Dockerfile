# Etapa build
FROM node:22-alpine AS build
WORKDIR /app
COPY packege*.json ./
RUN npm ci
COPY . .
RUN npm run build

# runtime
FROM node:22-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY packege*.json ./
RUN npm ci --omit=dev && npm cache clean --force

COPY --from=build /app/dist ./dist

USER node
CMD ["node", "dist/index.js"]