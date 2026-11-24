#!/usr/bin/env ruby
# Local preview without Jekyll: renders the pages with Liquid 4.0.4 (same as
# GitHub Pages) plus a few Jekyll-like filters/tags, and kramdown (GFM), into
# _preview/. site.github.releases is fetched from the GitHub API.
#
#   gem install --user-install liquid -v 4.0.4
#   gem install --user-install kramdown kramdown-parser-gfm
#   ruby _tools/preview.rb [--refresh]
require 'fileutils'
require 'json'
require 'kramdown'
require 'kramdown-parser-gfm'
require 'liquid'
require 'net/http'
require 'yaml'

ROOT = File.expand_path('..', __dir__)
OUT = File.join(ROOT, '_preview')

def markdown(text)
  Kramdown::Document.new(text.to_s, input: 'GFM', hard_wrap: false).to_html
end

module JekyllLikeFilters
  def relative_url(path)
    path = path.to_s.sub(%r{^/}, '')
    path.empty? ? 'index.html' : path
  end

  def markdownify(text)
    markdown(text)
  end

  def slugify(text)
    text.to_s.downcase.gsub(/[^a-z0-9]+/, '-').gsub(/^-|-$/, '')
  end

  def where(items, key, value)
    Array(items).select { |i| i[key].to_s == value.to_s }
  end
end
Liquid::Template.register_filter(JekyllLikeFilters)

# Jekyll-style {% include file.ext key=value %}.
class JekyllInclude < Liquid::Tag
  def initialize(tag, markup, tokens)
    super
    @file, rest = markup.strip.split(/\s+/, 2)
    @params = (rest || '').scan(/(\w+)=([\w.\[\]"']+)/)
  end

  def render(context)
    src = File.read(File.join(ROOT, '_includes', @file))
    context.stack do
      context['include'] = @params.to_h do |k, v|
        [k, v =~ /^["']/ ? v[1..-2] : context[v]]
      end
      Liquid::Template.parse(src).render(context)
    end
  end
end
Liquid::Template.register_tag('include', JekyllInclude)

# Rough stand-in for jekyll-seo-tag's {% seo %}.
class SeoTag < Liquid::Tag
  def render(context)
    site = context['site']
    page = context['page']
    title = page['title'] ? "#{page['title']} | #{site['title']}" : "#{site['title']} | #{site['description']}"
    desc = page['description'] || site['description']
    %(<title>#{title}</title>\n  <meta name="description" content="#{desc}">)
  end
end
Liquid::Template.register_tag('seo', SeoTag)

def releases(refresh)
  cache = File.join(ROOT, '_raw', 'releases.json')
  if refresh || !File.exist?(cache)
    FileUtils.mkdir_p(File.dirname(cache))
    uri = URI('https://api.github.com/repos/hungte/pietty/releases?per_page=100')
    File.write(cache, Net::HTTP.get(uri))
  end
  JSON.parse(File.read(cache))
end

def split_front_matter(src)
  _, fm, body = src.split(/^---\s*$/, 3)
  [YAML.safe_load(fm), body]
end

config = YAML.load_file(File.join(ROOT, '_config.yml'))
site = config.merge('github' => { 'releases' => releases(ARGV.include?('--refresh')) })
layout = File.read(File.join(ROOT, '_layouts', 'default.html'))

FileUtils.rm_rf(OUT)
FileUtils.mkdir_p(OUT)
FileUtils.cp_r(File.join(ROOT, 'assets'), OUT)
FileUtils.cp(File.join(ROOT, 'favicon.ico'), OUT)

%w[index.md download.html faq.md].each do |file|
  meta, body = split_front_matter(File.read(File.join(ROOT, file)))
  page = meta.merge('url' => meta['permalink'])
  vars = { 'site' => site, 'page' => page }
  tmpl = Liquid::Template.parse(body, error_mode: :strict)
  html = tmpl.render!(vars, strict_variables: false)
  html = markdown(html) if file.end_with?('.md')
  out = Liquid::Template.parse(layout).render!(vars.merge('content' => html))
  name = file.sub(/\.md$/, '.html')
  File.write(File.join(OUT, name), out)
  puts "wrote _preview/#{name}"
end
