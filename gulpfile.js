'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync').create();
var runsequence = require('run-sequence');
var reload = browserSync.reload;

var directoryjs = './medical_prescription/**/*.js'
var directorycss = './medical_prescription/**/*.css'
var directoryhtml = './medical_prescription/**/*.html'

var dist = "./dist"

gulp.task('browserSync', function() {
  browserSync.init({
    open: false,
    notify: false,
    proxy: 'localhost:8000'
  })
});

gulp.task('watch', function() {
  gulp.watch(directoryjs,['buildjs']);
  gulp.watch(directoryhtml,['buildhtml']);
  gulp.watch(directorycss,['buildcss']);
});

gulp.task('reload', function() {
  gulp.watch(directoryjs).on('change', browserSync.reload);
  gulp.watch(directoryhtml).on('change', browserSync.reload);
  gulp.watch(directorycss).on('change', browserSync.reload);
});

gulp.task('buildjs', function() {
  return gulp.src(directoryjs)
    .pipe(gulp.dest(dist));
});

gulp.task('buildhtml', function() {
  return gulp.src(directoryhtml)
    .pipe(gulp.dest(dist));
});

gulp.task('buildcss', function() {
  return gulp.src(directorycss)
    .pipe(gulp.dest(dist));
});

gulp.task('build', function(cb) {
  runsequence('buildjs','buildcss','buildhtml', cb);
});

gulp.task('default',['browserSync', 'watch','reload']);
