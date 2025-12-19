import { defineConfig } from "@remix-run/dev";
import { flatRoutes } from "remix-flat-routes";

export default defineConfig({
  ignoredRouteFiles: ["**/*.css"],
  routes: async (defineRoutes) => {
    return flatRoutes("routes", defineRoutes);
  },
});
