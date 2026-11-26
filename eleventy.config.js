export default function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy({ "src/images": "images" });
  eleventyConfig.addPassthroughCopy({ "src/media": "media" });
  eleventyConfig.addPassthroughCopy({ "src/portfolio": "portfolio" });
  eleventyConfig.addPassthroughCopy({ "src/soft-epilogue": "soft-epilogue" });
  eleventyConfig.addPassthroughCopy({ "src/contact": "contact" });
  eleventyConfig.addPassthroughCopy({ "src/index.html": "index.html" });
  eleventyConfig.addPassthroughCopy({ "src/404.html": "404.html" });
  eleventyConfig.addPassthroughCopy({ "src/favicon.svg": "favicon.svg" });

  // Keep line breaks as written, so poems keep their shape
  eleventyConfig.amendLibrary("md", (md) => md.set({ breaks: true, html: true, typographer: false }));

  const fmt = (d, opts) => new Intl.DateTimeFormat("en-GB", { timeZone: "UTC", ...opts }).format(new Date(d));
  eleventyConfig.addFilter("shortDate", (d) =>
    new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "short", day: "numeric", year: "numeric" }).format(new Date(d)));
  eleventyConfig.addFilter("dayMonthYear", (d) =>
    new Intl.DateTimeFormat("en-GB", { timeZone: "UTC", day: "numeric", month: "long", year: "numeric" }).format(new Date(d)));
  eleventyConfig.addFilter("longDate", (d) =>
    new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "long", day: "numeric", year: "numeric" }).format(new Date(d)));

  return {
    dir: { input: "src", output: "_site", includes: "_includes" },
    templateFormats: ["md", "njk"],
    markdownTemplateEngine: false,
  };
}
