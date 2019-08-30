from http.server import BaseHTTPRequestHandler
from cowpy import cow
import random
import re 

class handler(BaseHTTPRequestHandler):

  """ Generate ideas for code network projects """
  productions = {
      'tech': [
          'HTML5',
          'WebAssembly',
          'CoffeeScript',
          'pug',
          'jQuery',
          'Assembly',
          'Mashups',
          'puppeteer',
          'Bootstrap',
          'jango',
          'CSS',
          'git',
          'Java',
          'Bash',
          'Monads',
          'AI',
          'R',
          'Rust'
      ],

      'other': [
          'facial recognition',
          'coffee',
          'Blockhain',
          'vim',
          'facebook',
          'minecraft',
          'code network'
      ],

      'person': [
          'river city labs',
          'cats',
          'code network',
          'peter laurie'
      ],

      # pp = preposition phrase
      'pp': [
          'in 140 characters',
          'in small pieces',
          'on a Raspberry Pi',
          'in two days',
          'FTW'
      ],

      'talk': [
          '${tech} for ${person}',
          '${tech} + ${tech} = awesome',
          '${tech} with ${other}',
          '${tech} and ${other}',
          '${tech} ${pp}',
          'How to use ${tech} to make an amazing mess',
      ]
  }

  def randomly_generated(nt):
      template = random.choice(productions[nt])
      def replace(match):
          return randomly_generated(match.group(1))
      return re.sub(r'\$\{(\w+)\}', replace, template)

  def do_GET(self):
      self.send_response(200)
      self.send_header('Content-type','text/plain')
      self.end_headers()
      message = cow.Cowacter().milk(randomly_generated('talk'))
      self.wfile.write(message.encode())
      return
